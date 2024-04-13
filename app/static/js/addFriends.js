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