async function getText() {
    let url = 'http://192.168.68.112:8000/humidity';

    let response = await fetch(url);
    console.log(response.statusText);
    console.log(response.status);
    const cheese = await response.json()

    if (response.status === 200){
        let html = cheese.humidity;
        let containerHumid = document.querySelector('.containerHumid');
        containerHumid.innerHTML = html;
    }
    else{
        let html = '<p>no</p>';
        let containerHumid = document.querySelector('.containerHumid');
        containerHumid.innerHTML = html;
    }
}
getText()