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
					 
					 .state('Side.view_orders',{
                     url:'/view_orders',
                     views: {
                    'appContent' :{
                      templateUrl: 'view_orders.html',
                      controller : 'Ctrl'
                    }
                    }               
                     })
					 
					 .state('Side.view_orders.home',{
                     url:'/home',
                     views: {
                    'appContent' :{
                      templateUrl: 'home.html',
                      controller : 'Ctrl'
                    }
                    }               
                     })
					 .state('Side.view_orders.other',{
                     url:'/other',
                     views: {
                    'appContent' :{
                      templateUrl: 'other.html',
                      controller : 'Ctrl'
                    }
                    }               
                     })
					 .state('Side.view_orders.fav',{
                     url:'/fav',
                     views: {
                    'appContent' :{
                      templateUrl: 'fav.html',
                      controller : 'Ctrl'
                    }
                    }               
                     })
					 .state('Side.view_orders.settings',{
                     url:'/settings',
                     views: {
                    'appContent' :{
                      templateUrl: 'settings.html',
                      controller : 'Ctrl'
                    }
                    }               
                     })
					 
					

              .state('Side.profile',{
                       url:'/profile',
                       views: {
                      'appContent' :{
                        templateUrl: 'profile.html',
                        controller : 'Ctrl'
                      }
                      }               
                     })
              .state('Side.delivery',{
                       url:'/delivery',
                       views: {
                      'appContent' :{
                        templateUrl: 'delivery.html',
                        controller : 'Ctrl'
                      }
                      }               
                     })
              .state('Side.promotion',{
                       url:'/promotion',
                       views: {
                      'appContent' :{
                        templateUrl: 'promotion.html',
                        controller : 'Ctrl'
                      }
                      }               
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

              .state('profile',{
                      url:'/profile',
                      templateUrl:'profile.html',
                      comtroller:'Ctrl'
                      })
              .state('delivery',{
                      url:'/delivery',
                      templateUrl:'delivery.html',
                      comtroller:'Ctrl'
                      })
              .state('promotion',{
                      url:'/promotion',
                      templateUrl:'promotion.html',
                      comtroller:'Ctrl'
                      })
 $urlRouterProvider.otherwise('/Page1');
    });