/**
 * Favorite
 * @namespace dashBoardApp.favorite.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.services')
        .factory('Favorite', Favorite);

    Favorite.$inject = ['$http'];

    /**
     * @namespace Favorite
     * @returns {Factory}
     */
    function Favorite($http) {

        var Favorite = {
            get_favorites: getFavorites,
            toggle_favorites: toggleFavorite
        };

        function getFavorites(){
            return $http.get('/api/v1/favorites/');
        }

        /**
         * Call servite to add or remove favorite
         * @param favorite
         * @returns {HttpPromise}
         */
        function toggleFavorite(favorite) {
            return $http.post('/api/v1/favorites/', {target_object_id: favorite.id});
        }


        return Favorite;
    }
})()