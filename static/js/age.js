function ageCount() {
    var date1 = new Date();
    var dob = document.getElementById("dob").value;
    var date2 = new Date(dob);
    var pattern = /^\d{1,2}\/\d{1,2}\/\d{4}$/;
    //Regex to validate date format (dd/mm/yyyy)       
    if (pattern.test(dob)) {
        var y1 = date1.getFullYear();
        //getting current year            
        var y2 = date2.getFullYear();
        //getting dob year            
        var age = y1 - y2;
        //calculating age                       
        document.getElementById("ageId").value = age;
        document.getElementById("ageId").focus ();
        return true;
    } else {
        alert("Invalid date format. Please Input in (dd/mm/yyyy) format!");
        return false;
    }

}
