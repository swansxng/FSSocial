const findSearch = document.querySelector('.find');
const findResults = document.querySelector('.find_results');

$("#find").on('input', function() {
    FindFetchOnServer(findSearch.value)
});

async function FindFetchOnServer(request){
    const response = await fetch("/finder", {
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({'request': request})
    });
    console.log(await response.json())
}

document.addEventListener('click', (e) => {
    const onFindSearch = e.composedPath().includes(findSearch);
       if (onFindSearch) {
            findResults.style.display = 'flex';
       }
       else{
            findResults.style.display = 'none';
       }
})