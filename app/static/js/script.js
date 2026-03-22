async function sendMessage() {
    const messageInput = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");
    const message = messageInput.value.trim();

    if (!message) return; // Don't send empty messages

    // 1. Add User Message to Chat
    chatBox.innerHTML += `<div class="chat-message user-message"><b>You:</b> ${message}</div>`;
    messageInput.value = ""; // Clear input immediately

    // 2. Show Loading Indicator
    const loadingId = "loading-" + Date.now();
    chatBox.innerHTML += `<div id="${loadingId}" class="chat-message ai-message placeholder-text"><b>AI:</b> Typing...</div>`;
    
    // Auto-scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // 3. Fetch from Backend
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                phone_number: "1234567890", // Ideally, pull this dynamically if logged in
                message: message,
                language: "en"
            })
        });

        const data = await response.json();

        // 4. Replace Loading Indicator with Real Response
        document.getElementById(loadingId).outerHTML = `<div class="chat-message ai-message"><b>AI:</b> ${formatResponse(data.response)}</div>`;

    } catch (error) {
        document.getElementById(loadingId).outerHTML = `<div class="chat-message ai-message" style="color: red;"><b>System:</b> Error connecting to AI. Please try again.</div>`;
    }
    
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Reusable formatter for chat as well
function formatResponse(text) {
    if (!text) return "";
    return text.replace(/\n/g, "<br>");
}