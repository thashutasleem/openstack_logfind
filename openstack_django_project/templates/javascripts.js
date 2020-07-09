function validate_date()
    {
      var from_date = document.forms["check_date"]["FromDate"].value;
      var to_date = document.forms["check_date"]["ToDate"].value;
        
        var FromDate = new Date(from_date);
        var ToDate = new Date(to_date);
          
            if(FromDate > ToDate)
            {
                alert("From Date should be less than To Date");
                return false; 
            }
        }