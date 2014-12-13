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
        var msgs = { getMsgs:getMsgs, getMsg:getMsg };

        function getMsgs(folder){
            return $http.get('/api/v1/messages/' + folder);
        }

        function getMsg(id){
            return $http.get('/api/v1/messages/' + id);
        }

        return msgs;
  });