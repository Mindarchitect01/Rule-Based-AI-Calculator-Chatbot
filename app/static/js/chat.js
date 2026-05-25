document.getElementById('send-btn').addEventListener('click', sendMessage)
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') sendMessage();
});

function appendMessage(sender, text) {
    let chatBox = document.getElementById('chat-box');
    let msgDiv = document.createElement('div');
    msgDiv.className = sender === 'user' ? 'message user-message' : 'message bot-message';
    msgDiv.innerText = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    let inputField = document.getElementById('user-input');
    let message = inputField.value.trim();
    if (message === '') return;
    appendMessage('user', message);

    try {
        let response = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        })
        let data = await response.json();
        if (data.error) {
            appendMessage('bot', data.error);
        } else {
            appendMessage('bot', data.result);
        }
    } catch (err) {
        appendMessage('bot', 'Error: Tidak dapat menghubungi server.');
        console.error(err);
    }
    inputField.value = '';
}