

$(function(){
        $("form[name='login']").validate({

          rules:{
            email:{required:true,email:true}
          },
          messages:{email:"please Enter a valid Email"},
           submitHandler: function(form) {
            form.submit();
             }

          
        });
      });

 $(function(){
        $("form[name='myForm']").validate({

          rules:{
            email:{required:true,email:true},pass: {required: true,minlength: 5},cpass:{equalTo:"#pwd"}
          },
          messages:{email:"please Enter a valid Email",pass:{required: "Please provide password",minlength: "Your password must be at least 5 characters long!"},cpass:"password should be same"},
           submitHandler: function(form) {
            form.submit();
             }

          
        });
      });
$(function(){
        $("form[name='myadminForm']").validate({

          rules:{
            username:{required:true},pwd: {required: true,minlength: 5},cpwd:{equalTo:"#pwd"}
          },
          messages:{username:"please provide username",pwd:{required: "Please provide a password",minlength: "Your password must be at least 5 characters long"},cpwd:"password should be same"},
           submitHandler: function(form) {
            form.submit();
             }
             });
      });

  $(function(){
        $("form[name='adminlogin']").validate({

          rules:{
            username:{required:true},pwd:{required:true}
          },
           submitHandler: function(form) {
            form.submit();
             }

          
        });
      });
$(function(){
        $("form[name='appointment']").validate({

          rules:{
            vhnum:{required:true},mob: {required: true,minlength: 10,maxlength:13},city:{required:true},date:{required:true},sel_apt:{required:true}
          },
          messages:{email:"please provide Vehicle Number",mob:{required: "Please provide Mobile Number",minlength: "Enter Valid Mobile Number"}},
           submitHandler: function(form) {
            form.submit();
             }

          
        });
      });



$(function(){
  $('#m_datepicker_1').on('change',function(event){
    $.ajax({
      data:
      {
        date:$('input[name="date"]').val(),
        veh_typ:$('input[name="opt"]:checked').val()
      },
      type:'post',
      url:'/ajaxcall'
    })
    .done(function(data){
      $("#sel_apt").find('option').remove().end()
      
      for(var item in data.list)
      { 
        $("#sel_apt").append("<option value ="+data.list[item]+">"+data.list[item]+"</option>");

         // $("#sel_apt").append("<option value ="+data.list[item]+"+">"+"data.list[item]"."</option>");
        // console.log(data.list[item]) ;
      }

    });
    event.preventDefault();
  });
});


$(function(){
  $("#web").click(function(){
    
    $("#web_t").show(100);
    $("#sys_t").hide(100);
  });
  $("#sys").click(function(){
    
    $("#sys_t").show(100);
    $("#web_t").hide(100);
  })
})
