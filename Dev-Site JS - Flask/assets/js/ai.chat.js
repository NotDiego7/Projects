uploadButton = document.getElementById('upload-image-button');
uploadButton.addEventListener('click', handleUpload);

function handleUpload() {
  const input = document.createElement('input');

  input.type = 'file';
  input.accept = 'image/*';
  input.click();

  input.addEventListener('change', async () => {
    uploadButton.disabled = true;
    // Display Image
    const file = input.files[0];
    const imageURL = URL.createObjectURL(file);
  
    const imageElement = document.getElementById('image-preview');
    imageElement.src = imageURL;
    
    // File to send to server-side
    const imageBlob = file.slice(0, file.size, file.type);
    const reader = new FileReader();
  
    reader.onloadend = function () {
      const imageBase64 = reader.result.split(',')[1];
      localStorage.setItem('imageBase64', imageBase64);
  
      sendMessageButton = document.getElementById('send-message-button');
      sendMessageButton.addEventListener('click', getGoogleGeminiResponse);
    };
  
    reader.readAsDataURL(imageBlob);
  });
}


async function getGoogleGeminiResponse() {
  try {
    const imageBase64 = localStorage.getItem('imageBase64');
    const text = document.getElementById('message').value;

    // Send request to server-side proxy (Python) with streaming
    const response = await fetch('https://notdiego7.pythonanywhere.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        prompt: text,
        imageBase64: imageBase64,
      }),
    });

    const reader = response.body.getReader();

    while (true) {
      const { done, value } = await reader.read();

      if (done) {
        break;
      }

      // Update the UI with the streamed text
      const generatedText = document.querySelector('p#ai-body-text');
      generatedText.innerText += value;
    }

  } catch (error) {
    console.error(`Error: ${error}`);
  }
}
