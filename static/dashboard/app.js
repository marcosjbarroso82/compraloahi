angular.module('dashBoardApp', [
  'ui.router',
  'ngResource',
  'dashBoardApp.services',
  'dashBoardApp.controllers',
])
  .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    // Django expects jQuery like headers
    // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

    // Routing

    $urlRouterProvider.otherwise('/');

    $stateProvider
      .state('my-ads', {
        url: '/my-ads',
        templateUrl: '/static/dashboard/partials/ad-list.html',
        controller: 'AdCtrl',
      })
      .state('users', {
        url: '/users',
        templateUrl: '/static/dashboard/partials/user-list.html',
        controller: 'UserCtrl',
      })

  });