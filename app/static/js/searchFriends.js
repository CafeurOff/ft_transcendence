const searchInput = document.getElementById("search");
const usersContainer = document.getElementById("users");

searchInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        fetch(searchUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                'search': searchInput.value
            })
        })
        .then(response => response.json())
        .then(response => {
            usersContainer.innerHTML = '';

            if (response.users.length === 0) {
                usersContainer.innerHTML = `
                    <div class="col-12 d-flex justify-content-center">
                        <p class="fw-bold fs text-white">Aucun utilisateur trouvé</p>
                    </div>
                `;
            } else {
                response.users.forEach((user) => {
                    usersContainer.innerHTML += `
                        <div class="col-4 d-flex justify-content-center">
                            <div class="user-card p-3 bg-dark text-white">
                                <img src="${user.profile_image}" class="rounded-circle" width="100" height="100">
                                <p class="fw-bold fs-5 text-center">${user.username}</p>

                                <div class="d-flex justify-content-center items-center">
                                    <button class="btn btn-primary" onclick="addFriend('${user.username}')">Ajouter</button>
                                </div>
                            </div>
                        </div>
                    `;
                });
            }
        });
    }
});
