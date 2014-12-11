// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

//adServices.js

angular.module('dashBoardApp.services', ['ngResource'])
    .factory('Ad', function($resource) {
        return $resource('/api/v1/ads/:id/')
    })
    .factory('User', function($resource) {
        return $resource('/api/v1/users/:id/');
    });