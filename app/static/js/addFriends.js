// Autor: Lorenzo
// Function that sends a POST request to add a friend to the user's friend list

function addFriend(id) {
    fetch(addFriendUrl, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({
            'id': id
        })
    })

    .then(response => response.json())
    .then(response => {
        console.log(response);
    });
}