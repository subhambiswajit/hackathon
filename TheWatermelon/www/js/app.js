angular.module('starter', ['ionic','starter.controllers'])

.constant('ApiEndpoint',{
        url: 'http://localhost:8100/api/'
     })

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(false);
    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})


.config(function($stateProvider, $urlRouterProvider) {

  $stateProvider
        
		.state('Sidemenu',{
               url: '/Sidemenu',
               templateUrl:'Sidemenu.html',
         abstract: true,
               controller:'Ctrl'
               })
     /*   .state('Sidemenu.dashboard',{
               url:'/dashboard',
         views: {
        'appContent' :{
          templateUrl: 'dashboard.html',
          controller : 'Ctrl'
        }
      }               
               }) */
		       
        .state('Page1',{
               url: '/Page1',
               templateUrl:'Page1.html',
               controller:'Ctrl'
               })
    .state('Side',{
               url: '/Side',
               templateUrl:'Side.html',
         abstract: true,
               controller:'Ctrl'
               })
        .state('Side.dash',{
               url:'/dash',
         views: {
        'appContent' :{
          templateUrl: 'dash.html',
          controller : 'Ctrl'
        }
      }               
               })
        .state('Page3',{
               url: '/Page3',
               templateUrl:'Page3.html',
               controller:'Ctrl'
               })
    .state('Page4',{
               url: '/Page4',
               templateUrl:'Page4.html',
               controller:'Ctrl'
               })
    .state('Page5',{
               url: '/Page5',
               templateUrl:'Page5.html',
               controller:'Ctrl'
               })
    .state('Page6',{
               url: '/Page6',
               templateUrl:'Page6.html',
               controller:'Ctrl'
               })
    .state('Page7',{
               url: '/Page7',
               templateUrl:'Page7.html',
               controller:'Ctrl'
               })
    .state('signup',{
               url: '/signup',
               templateUrl:'Signup.html',
               controller:'Ctrl'
               })
    .state('dashboard',{
                url:'/dashboard',
                templateUrl:'dashboard.html',
                controller:'Ctrl'
                })
 $urlRouterProvider.otherwise('/Page1');
    });