// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()


angular.module('dashBoardApp.services', ['ngResource'])
    .factory('User', function($resource) {
        return $resource('/api/v1/users/:id/');
    })
    .factory('UserLocations', function($resource) {
        return $resource('/api/v1/user-locations/:id', { id: '@id' }, {
            update: {
                method: 'PUT' // this method issues a PUT request
            }
        });
    })
 ;
