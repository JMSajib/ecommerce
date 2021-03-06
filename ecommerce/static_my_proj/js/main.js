$(document).ready(function(){
  //Cntact from handler
  var contactForm = $(".contact-form")
  var contactFormMethod = contactForm.attr("method")
  var contactFormEndpoint = contactForm.attr("action")
  contactForm.submit(function(event){
    event.preventDefault()
    var contactFormData = contactForm.serialize()
    var thisForm = $(this)
    $.ajax({
      method: contactFormMethod,
      url: contactFormEndpoint,
      data: contactFormData,
      success:function(data){
        thisForm[0].reset()
        $.alert(
          {
            title:"Success",
            content:data.message,
            theme:"modern",
          })
      },
      error:function(error){
        console.log(error.responseJSON)
        var jsonData = error.responseJSON
        var msg = ""
        $.each(jsonData,function(key,value){
          msg += value[0].message + "<br>"
        })
        $.alert(
          {
            title:"Opps!!",
            content:msg,
            theme:"modern",
          })
      }
    })
  })

  // Auto Search
  var searchForm = $(".search-form")
  var searchInput = searchForm.find("[name='q']")
  var searchBtn = searchForm.find("[type='submit']")
  var typingTimer;
  var typingInterval = 500;

  searchInput.keyup(function(event){
    clearTimeout(typingTimer)
    typingTimer = setTimeout(performSearch,typingInterval)
  })

  searchInput.keydown(function(){
    clearTimeout(typingTimer)
  })

  function displaySearching(){
    searchBtn.addClass("disabled")
    searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching....").css("color","white")
  }

  function performSearch(){
    displaySearching()
    var query = searchInput.val()
    setTimeout(function(){
      window.location.href = '/search/?q=' + query
    },1000)

  }

  // Cart + Add product
  var productForm = $(".form-product-ajax")
  productForm.submit(function(event){
    event.preventDefault();
    var thisForm = $(this);
    // var actionEndpoint = thisForm.attr("action");
    var actionEndpoint = thisForm.attr("data-endpoint");
    var httpMethod = thisForm.attr("method");
    var formData = thisForm.serialize();

    $.ajax({
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function(data){
        var submitSpan = thisForm.find(".submit-span")
        if(data.added){
          submitSpan.html("In Cart <button type='submit' class='btn btn-link'>Remove?</button>")
        }
        else{
          submitSpan.html("<button type='submit' class='btn btn-success'>Add to cart</button>")
        }
        var itemCount = $(".cart-item")
        itemCount.text(data.cartItemCount)
        var currentPath = window.location.href
        if(currentPath.indexOf("cart") != -1){
          refreshCart()
        }
      },
      error: function(errorData){
        $.alert(
          {
            title:"Opps!!",
            content:"An Error occured!!",
            theme:"modern",
          })
      }
    })

  })
  function refreshCart(){
    console.log("In current Cart Now")
    var cartTable = $(".cart-table")
    var cartBody  = cartTable.find(".cart-body")
    var currentUrl = window.location.href
    // cartBody.html("<h1>Changed</h1>")
    var productsRows = cartBody.find(".cart-product")


    var refreshCartUrl = '/api/cart/';
    var refreshCartMethod = "GET";
    var data={};
    $.ajax({
      url: refreshCartUrl,
      method: refreshCartMethod,
      data: data,
      success: function(data){
        console.log("Success")
        var hiddenCartRemoveForm = $(".cart-item-remove-form")
        if(data.products.length > 0){
          productsRows.html(" ")
          i=data.products.length
          $.each(data.products,function(index,value){
            var newCartItemRemove = hiddenCartRemoveForm.clone()
            newCartItemRemove.css("display","block")
            newCartItemRemove.find(".cart-item-product-id").val(value.id)
            cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
            i--
          })
          cartBody.find(".cart-subtotal").text(data.subtotal)
          cartBody.find(".cart-total").text(data.total)
        }
        else{
          window.location.href = currentUrl
        }
      },
      error: function(errorData){
        $.alert(
          {
            title:"Opps!!",
            content:"An Error occured!!",
            theme:"modern",
          })
      }
    })
  }
})
