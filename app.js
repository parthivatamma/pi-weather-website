
async function getText() {
    let url = 'http://192.168.68.112:8000/temp';

    let response = await fetch(url);
    console.log(response.statusText);
    console.log(response.status);
    const cheese = await response.json()
    console.log(cheese)

    if (response.status === 200){
        let html = cheese.temp;
        let containerTemp = document.querySelector('.containerTemp');
        containerTemp.innerHTML = html;
    }
    else{
        let html = '<p>no</p>';
        let containerTemp = document.querySelector('.containerTemp');
        containerTemp.innerHTML = html;
    }
}
getText()