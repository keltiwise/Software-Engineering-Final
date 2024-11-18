# Software Engineering Final
## Static CSS
Using this CSS file, we personalized our website by adding buttons, changing font, adjusting our borders and margins, and adding padding. Using CSS, we were able to control the size of the map, which showcases all breweries in the United States, to our liking and added hover features. 

```CSS
.header {
  background-color: #1A1A1D;
  color: white;
  padding: 10px;
  text-align: left;
  height: 70px;
}

p {
  font-size: 20px;
}

#map {
  height: 600px;
  width: 90%;
  margin-top: 80px; 
  border: 4px solid #6F2232; 
  margin-left: auto; 
  margin-right: auto;
}

.topnav {
    background-color: #4E4E50 ;
    overflow: hidden;
  }
  
  .topnav a {
    float: left;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
    width: 200px
  }
  
  .topnav a:hover {
    background-color: #950740;
    color: white;
  }
  
  .topnav a.active {
    background-color: #6F2232;
    color: white;
  }

  body {
    background-color: grey;
  }


.marker-dot {
    position: relative;
    z-index: 1;
}

table {
  margin-top: 20px; 
  margin-left: 20px; 
  width: calc(100% - 40px); 
  border-collapse: collapse; 
}
th, td {
  padding: 10px; 
  border: 1px solid #ddd; 
}

.buttonUpdate,
.buttonAdd,
.buttonDelete{
  padding: 10px 20px;
  background-color: #6F2232;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  width: 100px;
}
.inputUpdate,
.inputAdd,
.inputDelete{
  padding: 10px;
  border: 1px solid black;
  border-radius: 5px;
  width: 150px;
  margin-top: 10px;
  margin-right: 10px;
}
.buttonContainer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin-right: 20px; 
}

.buttonContainer2 {
  display: flex;
  align-items: left; /* This property is not valid. You can remove it. */
  justify-content: flex-start; /* Align items to the left */
}

textarea {
  width: 90%; 
  height: 300px; 
  border: 4px solid #6F2232; 
}

select {
  padding: 10px 20px; 
  background-color: black; 
  color: white; 
  border: none; 
  border-radius: 5px; 
  cursor: pointer; 
  margin-top: 10px; 
  width: 100px; 
  appearance: none; 
}

```
