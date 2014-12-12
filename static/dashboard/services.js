// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

//adServices.js

angular.module('dashBoardApp.services', ['ngResource'])
  .factory('Ad', function($resource) {
    return $resource('/api/v1/ads/:id/')
  })
  .factory('User', function($resource) {
    return $resource('/api/v1/users/:id/');
  })
  /*
  .factory('Message', function($resource) {
    return $resource('/api/v1/messages/:id/');
  });
      */
  .factory('Message', function($resource, $http) {
        var msgs = {getMsgs:getMsgs};

        function getMsgs(folder){
            return $http.get('/api/v1/messages/' + folder);
        }
        return msgs;
  });