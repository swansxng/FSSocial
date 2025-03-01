async function postModal_showhide(post_id) {
    const element = document.getElementById("post_photo_full" + post_id);
    if (element.style.display == "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}