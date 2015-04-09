/**
 * Ad
 * @namespace App.ad.services
 */
(function () {
    'use strict';

    angular
        .module('App.ad.services')
        .factory('Ad', Ad);


    /**
     * @namespace Ad
     * @returns {Factory}
     */
    function Ad() {
        //return $resource('/api/v1/ads/:id/:page');
        return {
            get :function(callback){
                callback(json_data)

            }



        };
    }


})()