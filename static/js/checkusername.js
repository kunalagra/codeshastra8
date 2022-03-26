    $(document).ready(function(){
		$('#username').keyup( function(e){
            var username = $('#username').val();
            if(username != ''){
      
               $.ajax({
                  url: '/checkusername',
                  type: 'post',
                  data: {username: username},
                  success: function(response){
                        if (response == "Available"){
                      $('#uname_response').html(response).css({'color':'blue', 'text-align':'right'});
                      $('#button').removeAttr('disabled');
                        }else{
                            $('#uname_response').html(response).css({'color':'red', 'text-align':'right'});
                            $('#button').prop('disabled',true);
                        }
                   }
               });
            }else{
               $("#uname_response").html("");
               $('#button').prop('disabled',true);
            }
		})
	})