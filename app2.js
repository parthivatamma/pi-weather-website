async function getText() {
    let url = 'http://192.168.68.112:8000/pressure';

    let response = await fetch(url);
    console.log(response.statusText);
    console.log(response.status);
    const cheese = await response.json()

    if (response.status === 200){
        let html = cheese.pressure;
        let containerPres = document.querySelector('.containerPres');
        containerPres.innerHTML = html;
    }
    else{
        let html = '<p>no</p>';
        let containerPres = document.querySelector('.containerPres');
        containerPres.innerHTML = html;
    }
}
getText()