<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Reservation Form</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="{% static 'css/normalize.css' %}">
        <link rel="stylesheet" href="{% static 'css/main.css' %}">
        <script src="{% static 'js/vendor/modernizr-2.6.2.min.js' %}"></script>
        <script type="text/javascript" src="{% static 'lib/bootstrap-datepicker.js' %}"></script>
        <link rel="stylesheet" type="text/css" href="{% static 'lib/bootstrap-datepicker.css' %}" >

    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <!-- Add your site or application content here -->
        <form id="booking-form" class="booking-form" name="form1" method="post" action="cancel.php">
            <div align="center"><img class="logo" src="img/example_logo.png" title="Example Logo" alt="Example Logo"></div>
            <div class="h1">Cancel reservation  </div>
            <div id="form-message" class="message hide">
                Thank you for your enquiry!
            </div>
            <div id="form-content">
                
                
                <div class="group">
                    <label for="cusid">Name</label>
                    <div><input id="cusid" name="cusid" class="form-control" type="text" placeholder="Customer ID"></div>
                </div>

                <div class="group">
                    <label for="cnic">CNIC</label>
                    <div><input id="email" name="cnic" class="form-control" type="cnic" placeholder="CNIC"></div>
                </div>
                
                <div class="group submit">
                    <label class="empty"></label>
                    <div><input name="Delete" type="submit" value="Cancel"/></div>
                </div>
            </div>
            <div id="form-loading" class="hide"><i class="fa fa-circle-o-notch fa-spin"></i></div>
        </form>

        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>
    </body>
</html>
