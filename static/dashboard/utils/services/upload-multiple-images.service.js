/**
 * Item
 * @namespace dashBoardApp.item.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.util.services')
        .factory('ItemImages', ItemImages);

    ItemImages.$inject = ['$http'];

    /**
     * @namespace Item
     * @returns {Factory}
     */
    function ItemImages($http) {
        var Images = {
            create: create,
            destroy: destroy,
            //update: update,
            change_default: change_default
        };

        return Images;

        function destroy(image){
            return $http.delete('/api/v1/user-items-images/' + image.id + '/');
        }

        function create(image){
            var fd = new FormData();
            fd.append('default', image.default);
            fd.append('ad', image.ad);
            fd.append('image', image.resize_image);

            return $http.post('/api/v1/user-items-images/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

        function update(image){
            var fd = new FormData();
            fd.append('id', image.id);
            fd.append('default', image.default);
            if(image.resize_image){
                fd.append('image', image.resize_image);
            }
            return $http.put('/api/v1/user-items-images/' + String(image.id) + '/', fd, {
                headers: {'Content-Type': undefined},
                withCredentials: true,
                transformRequest: angular.identity
            });
        }

        function change_default(image){
            return $http.patch('/api/v1/user-items-images/'+ String(image.id) + '/', image);
        }

    }

})();