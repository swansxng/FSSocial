async function delete_post(post_id) {
    $.ajax({
        type: 'POST',
        url: '/delete_post',
        dataType: "json",
        data: JSON.stringify({'post_id': post_id}),
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        //TODO: correct incorrect response
        success: (data) => {
            const element = document.getElementById('post' + post_id);
            element.remove();
        }
        }
    )
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
