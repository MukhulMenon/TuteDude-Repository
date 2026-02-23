// express app that serves html files
const express = require('express');
const app = express();
app.set('view engine', 'ejs');

const URL = process.env.BACKEND_URL||'http://127.0.0.1:8000/api';

const fetch=(...args)=>
    import('node-fetch').then(({default: fetch})=>fetch(...args));

app.get('/', async function(req,res){
  const options = {
    method: 'GET'
};
  fetch(URL, options)
    .then(res => res.json())
    .then(json=>console.log(json))
    .catch(error => console.error('error:', error));
    try{
        let response = await fetch(URL, options);
        response = await response.json();
        res.render('index',response);
    }
    catch(error){
        console.error('Error fetching data:', error);
        res.status(500).send('Error fetching API data');    
    }
}); 

app.listen(3000, () => {
    console.log('Server is running on port 3000');
    });