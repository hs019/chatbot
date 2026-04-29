function sendMessage() {
    let input = document.getElementById("user-input");
    let chatBox = document.getElementById("chat-box");

    let userText = input.value.toLowerCase();

    if (userText.trim() === "") return;

    chatBox.innerHTML += `<p class="user">You: ${userText}</p>`;

    let botReply = getBotReply(userText);

    setTimeout(() => {
        chatBox.innerHTML += `<p class="bot">Bot: ${botReply}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 500);

    input.value = "";
}

function getBotReply(text) {
    if (text.includes("hi") || text.includes("hello")) {
        return "Hey there! 👋";
    } 
    else if (text.includes("how are you")) {
        return "I'm doing great 😎";
    } 
    else if (text.includes("name")) {
        return "I'm your chatbot!";
    } 
    else if (text.includes("bye")) {
        return "See you later! 👋";
    } 
    else {
        return "I don't get that 😅";
    }
}