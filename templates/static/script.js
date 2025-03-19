const socket = io();

// Listen for messages from the server
socket.on("receive_message", (data) => {
    const messages = document.getElementById("messages");
    const messageElement = document.createElement("div");
    messageElement.classList.add("flex", "items-center", "p-2", "border-b");

    messageElement.innerHTML = `
        <img src="${data.avatar_url}" alt="Avatar" class="w-8 h-8 rounded-full mr-2">
        <div>
            <strong class="text-gray-700">${data.username}</strong> <span class="text-xs text-gray-500">${data.timestamp}</span>
            <p class="text-gray-800">${data.content}</p>
        </div>
    `;

    messages.appendChild(messageElement);
    messages.scrollTop = messages.scrollHeight;
});

// Send message to server
function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const message = messageInput.value.trim();

    if (message) {
        socket.emit("send_message", { username: "User", message: message });
        messageInput.value = "";
    }
}
