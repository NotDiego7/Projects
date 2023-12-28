const uploadButton = document.getElementById('upload-image-button');

uploadButton.addEventListener('click', () => {
  const fileReader = new FileReader();

  // Function to handle the image data for display
  fileReader.onload = (event) => {
    const imageURL = event.target.result;
    const imageElement = document.getElementById('image-preview');
    imageElement.src = imageURL;
  };

  // Trigger the file selection dialog
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = 'image/*';
  input.click();

  input.addEventListener('change', () => {
    fileReader.readAsDataURL(input.files[0]); // Read as data URL for display

    // Upload image directly to Dropbox when the send button is clicked
    const sendMessageButton = document.getElementById('send-message-button');
    sendMessageButton.addEventListener('click', async () => {
      const imageFile = input.files[0];
      const reader = new FileReader();
      reader.readAsArrayBuffer(imageFile);

      reader.onloadend = async () => {
        try {
          // Upload image to Dropbox
          const response = await fetch('https://content.dropboxapi.com/2/files/upload', {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer sl.BsgkCgkvqmoDyafZQlA-sKFrqZJElcrjVTCNSgFUzkTeoTjiGbKnwozlLXEod3JzpHOd9T23rHpnyL2L2q8Oia3eR9F43N0QS_hKaN0XEykeFxFfWlQR2kGVOUYJ46suZtM5FdxVguheC90GUB5N',  // Replace with your access token
              'Content-Type': 'application/octet-stream',
              'Dropbox-API-Arg': JSON.stringify({
                path: '/image.jpg',
                mode: 'overwrite'
              })
            },
            body: reader.result
          });


          // Check if shared link already exists
          const existingSharedLinkResponse = await fetch('https://api.dropboxapi.com/2/sharing/list_shared_links', {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer sl.BsgkCgkvqmoDyafZQlA-sKFrqZJElcrjVTCNSgFUzkTeoTjiGbKnwozlLXEod3JzpHOd9T23rHpnyL2L2q8Oia3eR9F43N0QS_hKaN0XEykeFxFfWlQR2kGVOUYJ46suZtM5FdxVguheC90GUB5N',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              path: '/image.jpg',
              direct_only: true  // Only include direct shared links
            })
          });

          const existingSharedLinkData = await existingSharedLinkResponse.json();

          let dropboxPreviewPage;
          if (existingSharedLinkData.links.length > 0) {
            // Use existing shared link
            dropboxPreviewPage = existingSharedLinkData.links[0].url;
          } else {
            // Create shared link if it doesn't exist
            const createSharedLinkResponse = await fetch('https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings', {
              method: 'POST',
              headers: {
                'Authorization': 'Bearer sl.BsgkCgkvqmoDyafZQlA-sKFrqZJElcrjVTCNSgFUzkTeoTjiGbKnwozlLXEod3JzpHOd9T23rHpnyL2L2q8Oia3eR9F43N0QS_hKaN0XEykeFxFfWlQR2kGVOUYJ46suZtM5FdxVguheC90GUB5N',
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                path: '/image.jpg',
                settings: {
                  access: 'viewer',
                  allow_download: true,
                  audience: 'public',
                  requested_visibility: 'public'
                }
              })
            });

            const dropboxSharedLinkResponse = await createSharedLinkResponse.json();
            dropboxPreviewPage = dropboxSharedLinkResponse.url;
          }


          const text = document.getElementById('message').value;

          // Call Python server-side proxy with CORS in-place to make requests to Gemini API
          const pyProxyResponse = await fetch('https://notdiego7.pythonanywhere.com/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              prompt: text,
              dropboxPreviewPage: dropboxPreviewPage
            })
          });
          const ProxyResponse = await pyProxyResponse.json();
          const generatedText = ProxyResponse.text;

          document.querySelector('p#ai-body-text').innerText = generatedText;
        } catch (error) {
          console.error('Error:', error);
        }
      };
    });
  });
});
























































// const uploadButton = document.getElementById('upload-image-button');

// uploadButton.addEventListener('click', () => {
//   const fileReader = new FileReader();

//   // Function to handle the image data for display
//   fileReader.onload = (event) => {
//     const imageURL = event.target.result;
//     const imageElement = document.getElementById('image-preview');
//     imageElement.src = imageURL;
//   };

//   // Trigger the file selection dialog
//   const input = document.createElement('input');
//   input.type = 'file';
//   input.accept = 'image/*';
//   input.click();

//   input.addEventListener('change', () => {
//     fileReader.readAsDataURL(input.files[0]); // Read as data URL for display

//     // Send image bytes as a Blob when the send button is clicked
//     const sendMessageButton = document.getElementById('send-message-button');
//     sendMessageButton.addEventListener('click', () => {
//       const formData = new FormData();
//       formData.append('text', document.getElementById('message').value);

//       // Read image bytes directly
//       const imageFile = input.files[0];
//       const reader = new FileReader();
//       reader.readAsArrayBuffer(imageFile);

//       reader.onloadend = () => {
//         formData.append('imageBytes', new Blob([reader.result])); // Append image bytes as a Blob

//         fetch('https://notdiego7.pythonanywhere.com/', {
//           method: 'POST',
//           headers: {
//             'Content-Type': 'multipart/form-data'
//           },
//           body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//           document.querySelector('p#ai-body-text').innerText = data.text;
//         })
//         .catch(error => {
//           console.error('Error sending image data:', error);
//         });
//       };
//     });
//   });
// });
