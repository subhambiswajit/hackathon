angular.module('starter.controllers', [])

.controller('Ctrl',function($scope,$http,$state,$location,$ionicLoading,$timeout,$ionicSideMenuDelegate,ApiEndpoint){
            $scope.submit=function(user){
              $http({
      method: 'POST',
      url: ApiEndpoint.url+ 'login/',
      data: {       username: user.username,
                        password: user.password   
                    }
    }).then(function successCallback(response) {
        $scope.smuglers = [];
       for(var r in response.data) {
          var smugler = response.data[r]; 
        }
          $scope.smuglers.push(response);
          console.log($scope.smuglers);
          alert($scope.smuglers);
          $location.url('/Side/home');
        })
        
    }, function errorCallback(response) {
        console.log("ERROR");
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
      $location.url('/Side/home');
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
  };
  
            });