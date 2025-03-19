const socket = io();

socket.on("connect", () => {
    console.log("Connected to server");
});

socket.on("receive_message", (data) => {
    const messages = document.getElementById("messages");
    const messageElement = document.createElement("p");
    messageElement.textContent = `${data.username}: ${data.message}`;
    messages.appendChild(messageElement);
});

function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const message = messageInput.value;
    socket.emit("send_message", { username: "User", message: message });
    messageInput.value = "";
}
