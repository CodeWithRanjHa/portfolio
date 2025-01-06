function getdata() {
    const  url = "http://127.0.0.1:8000/category";
    fetch(url)
    .then(response => response.json())    
}

