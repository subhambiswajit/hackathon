angular.module('starter.controllers', [])

.controller('Ctrl',function($scope,$http,$state,$location,$ionicLoading,$timeout,$ionicSideMenuDelegate,ApiEndpoint,$ionicPopup){
            $scope.items = [{id:1,name:'',price:'',image:''},{id:2,name:'',price:'',image:''}];
            $scope.submit=function(user){
                 if(user.username=='' || user.password=='')
				 {
					 $scope.showAlert("Field Empty!","Error");
					 user.username="";
					 user.password="";
				 }
				 else {
					$ionicLoading.show();
                  $http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'signin/',
                        data:{username:user.username, password:user.password}
                      }).then(function successCallback(response) {

                         
						 $scope.showAlert("Logged in successfully!","Logged in");
						$ionicLoading.hide();
						 //$location.url('/Side/dash');
						  user.password='';
						  

                          console.log("success");
                    if(response.data == "true")
                    {
      						    $scope.showAlert("Logged in successfully!","Logged in");
        						  $location.url('/Side/dash');
        						  user.password='';
                    }
               else if(response.data == "verify")
                {
                      $location.url('/otp');
                }
                else if(response.data == "False")
                {
                  $scope.showAlert("Username/Password does not exist!","Error");
                }

                      }, function errorCallback(response) {
						  $scope.showAlert("Error during login!","Internal Error");
						  user.password='';
                         
						  
				 });}
             
			
			}
			
			$scope.logout = function()
			{
				$http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'loggedout/',
                        data:{loggedout:1}
                      }).then(function successCallback(response) {
                          
						  
						  //$scope.showAlert("Signed up successfully!","Signed Up");
						 // $location.url('/Page1');
						  
                      }, function errorCallback(response) {
                          //console.log("ERROR");
						  //$scope.showAlert("Some field is empty !(error)");
						  
						  
                      });
			}
			
			$scope.signup = function(user)
			{
				if(user.email=='' || user.add == '' || user.pin=='' || user.phone == '' || user.pass == '')
					$scope.showAlert("Some field is empty!","Error");
				else{
					$ionicLoading.show();
				$http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'signup/',
                        data:{email:user.email, address:user.add, pincode:user.pin, phone:user.phone,password:user.pass}
                      }).then(function successCallback(response) {
                          
						  if(response.data == "True")
						  {
						  $ionicLoading.hide();
						  $scope.showAlert("Signed up successfully!","Signed Up");
						  $location.url('/Page1');
						  }
						  else
						  {
							  $ionicLoading.hide();
							$scope.showAlert("User already exists!","Alert");  
						  }
						  
                      }, function errorCallback(response) {
                          console.log("ERROR");
						  $ionicLoading.hide();
						  $scope.showAlert("Some field is empty!","Error");
						  
                      });

				}
                      user.email=='';
                      user.add == '';
                      user.pin=='';
                      user.phone == '';
                      user.pass == '';
			}
			$scope.verify = function(n,user) {
				if(n==0)
					$scope.showAlert("Another OTP will be sent shortly to your registered email id","Resend");
				$http({
                        method: 'POST',
                        url: ApiEndpoint.url+ 'verify_code/',
                        data:{otp:user.otp, verify:n}
                      }).then(function successCallback(response) {
						  if(response.data == "true")
						  {
							  $scope.showAlert("Verified successfully!","Success");
							  $location.url("/Side/dash");
						  }
              else if(response.data == "False")
						  {
							  $scope.showAlert("Invalid verification code!","Error");
							  user.otp = "";
						  }
					
                      }, function errorCallback(response) {
                          console.log("ERROR");
						  $scope.showAlert("Internal error during verification!","Internal error");
						  
                      });
			}
			$scope.showAlert = function(msg,head) {
   var alertPopup = $ionicPopup.alert({
     title: head,
     template: msg
	 
			});
$timeout(function() {
     alertPopup.close(); 
  }, 3000);
 			}
			$scope.hide = function(){
    $ionicLoading.hide();
  };
      
    /*  if(user.username == 'anusha' && user.password == 'anusha')
      {
      user.username="";
      user.password="";
            $location.url('/Side/home');
      }
      else
      {
      user.username="";
      user.password="";
      alert('Invalid information');}
       */

      $scope.save=function() {
      alert("Saved!");
      $location.url('/Side/dash');
      } 

      $ionicLoading.show({
    content: 'Loading',
    animation: 'fade-in',
    showBackdrop: true,
    maxWidth: 200,
    showDelay: 0
  })

   $timeout(function () {
   $ionicLoading.hide();},1000)

  $scope.toggleLeft = function() {
    $ionicSideMenuDelegate.toggleLeft();
  }

  $scope.signup_redirect = function(){
     $location.url('/signup');
  }
  
            });