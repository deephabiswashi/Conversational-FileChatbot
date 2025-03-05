document.addEventListener("DOMContentLoaded", function() {
  const uploadForm = document.getElementById("upload-form");
  const uploadStatus = document.getElementById("upload-status");
  const chatForm = document.getElementById("chat-form");
  const chatWindow = document.getElementById("chat-window");
  const themeToggle = document.getElementById("theme-toggle");
  const modelSelect = document.getElementById("model-select");

  // Theme toggle
  themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
  });

  // Handle file upload
  uploadForm.addEventListener("submit", function(e) {
    e.preventDefault();
    const fileInput = document.getElementById("file-input");
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    fetch("/upload", {
      method: "POST",
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        uploadStatus.textContent = "Error: " + data.error;
      } else {
        uploadStatus.textContent = data.message;
      }
    })
    .catch(err => {
      uploadStatus.textContent = "Upload failed.";
      console.error(err);
    });
  });

  // Handle chat form submission
  chatForm.addEventListener("submit", function(e) {
    e.preventDefault();
    const chatInput = document.getElementById("chat-input");
    const query = chatInput.value;
    const selectedModel = modelSelect.value;

    // Append user's message
    appendMessage("user", query);
    chatInput.value = "";

    fetch("/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({query: query, model: selectedModel})
    })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        appendMessage("bot", "Error: " + data.error);
      } else {
        appendMessage("bot", data.response);
      }
    })
    .catch(err => {
      appendMessage("bot", "Error processing request.");
      console.error(err);
    });
  });

  function appendMessage(sender, text) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);
    messageDiv.textContent = text;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
});
