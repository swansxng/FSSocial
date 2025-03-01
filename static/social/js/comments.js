async function sendComment(post_id, profile_id, my_id, my_name) {
    const textbox = document.getElementById("comment_write" + post_id);
    $.ajax({
        type: 'POST',
        url: '/add_comment',
        dataType: "json",
        data: JSON.stringify({'post_id': post_id, 'profile_id': profile_id, 'comment': textbox.innerText}),
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        success: (data) => {
            //TODO???
        }
        })
    let cmntblk = document.createElement('div');
    cmntblk.className = 'comment_block';
    cmntblk.style.display = 'flex';
    cmntblk.innerHTML = `<div class="comment_photo_data">
                            <img src="/static/social/images/defaults/empty%20user%20image/camera_400.png" class="profile_img" width="34" height="34">
                        </div>
                        <div class="comment_info_data">
                            <a class="comment_author" href="/id${my_id}">${ my_name }</a>
                            <div class="comment_text">${ textbox.innerText }</div>
                        </div>`;
    textbox.innerText = "";
    let to_append = document.getElementById("post_comments" + post_id);
    to_append.append(cmntblk);
}
