// Check if we already have an access token from the previous run (using localStorage)
// If not, get it by running the authorization flow; otherwise, continue with the flow
const storedAccessToken = localStorage.getItem('accessToken');

if (!storedAccessToken) {
  authorizeDropbox();
} else {
  // Continue with the flow using the stored access token
  uploadButton.addEventListener('click', handleUpload);
}

function authorizeDropbox() {
  // Receives authorization URL | /auth-step-one
  fetchAuthorizationURL();
  
  // Clear message input value to avoid issues
  document.getElementById('message').value = '';

  const sendAuthorizationCodeButton = document.getElementById('send-message-button');
  sendAuthorizationCodeButton.onclick = async () => {
    const authorizationCode = document.getElementById('message').value;
    await postAuthorizationCode(authorizationCode);
  };
}

async function fetchAuthorizationURL() {
  const authorizationStepOneResponse = await fetch('https://notdiego7.pythonanywhere.com/auth-step-one', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  const authorizationURL = await authorizationStepOneResponse.json().authorizationURL; // NOTE: Might need to add to local Storage
  console.log(`Authorization Page Buddyyyyyy: ${authorizationURL}`)
  document.querySelector('p#ai-body-text').innerText = `Authorization Page: ${authorizationURL}`;
}

async function postAuthorizationCode(authorizationCode) {
  // POST requests transporting authorization code. | /auth-step-two
  const authorizationStepTwoResponse = await fetch('https://notdiego7.pythonanywhere.com/auth-step-two', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      authorizationCode,
    })
  });

  const longLivedAccessToken = await authorizationStepTwoResponse.json().longLivedAccessToken;
  console.log(`This is the long-lived access token ${longLivedAccessToken}`);
  localStorage.setItem('accessToken', longLivedAccessToken);

  // Continue with the flow using the obtained access token
  uploadButton.addEventListener('click', handleUpload);
}

function handleUpload() {
  const fileReader = new FileReader();
  const input = document.createElement('input');

  input.type = 'file';
  input.accept = 'image/*';
  input.click();

  input.addEventListener('change', () => {
    fileReader.readAsDataURL(input.files[0]); // Read as data URL for display

    fileReader.onload = async (event) => {
      const imageURL = event.target.result;
      const imageElement = document.getElementById('image-preview');
      imageElement.src = imageURL;

      const longLivedAccessToken = localStorage.getItem('accessToken');
      await uploadImageToDropbox(input.files[0], longLivedAccessToken);
    };
  });
}

async function uploadImageToDropbox(imageFile, accessToken) {
  const reader = new FileReader();
  reader.readAsArrayBuffer(imageFile);

  reader.onloadend = async () => {
    try {
      // Upload image to Dropbox
      const response = await fetch('https://content.dropboxapi.com/2/files/upload', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/octet-stream',
          'Dropbox-API-Arg': JSON.stringify({
            path: '/image.jpg',
            mode: 'overwrite'
          })
        },
        body: reader.result
      });

      // Get temporary link using /get_temporary_link
      const temporaryLinkResponse = await fetch('https://api.dropboxapi.com/2/files/get_temporary_link', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          path: '/image.jpg'
        })
      });

      const temporaryLink = await temporaryLinkResponse.json().link; // Get temporary link
      const text = document.getElementById('message').value;

      // Send request to server-side proxy (Python) | CORS(request) -> Gemini API -> Response
      const pyProxyResponse = await fetch('https://notdiego7.pythonanywhere.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          prompt: text,
          temporaryLink: temporaryLink
        })
      });

      const generatedText = await pyProxyResponse.json().text;
      document.querySelector('p#ai-body-text').innerText = generatedText;
    } catch (error) {
      console.error('Error:', error);
    }
  };
}
