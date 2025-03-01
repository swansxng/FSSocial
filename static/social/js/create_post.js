async function postCreate_showhide() {
    const element = document.getElementById("create_post");
    if (element.style.display == "none") {
        element.style.display = "block";
        document.getElementById('dbb').textContent = 'Hide';
    } else {
        element.style.display = "none";
        document.getElementById('dbb').textContent = 'Create post';
    }
}

