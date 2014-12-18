/**
 * AdCtrl
 * @namespace dashBoardApp.ad.controllers
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.controllers')
        .controller('AdCtrl', AdCtrl);

    AdCtrl.$inject = ['$scope', 'Ad'];

    /**
     * @namespace AdCtrl
     */
    function AdCtrl($scope, Ad) {
        $scope.ads = {};
        $scope.next_page = null;
        $scope.prev_page = null;

        Ad.get(function(response) {
            console.log(response);
            $scope.ads = response.results;
            $scope.count_page = response.count;
            $scope.next_page = response.next;
            $scope.prev_page = response.previous;

        });
        $scope.get_ads_page = function(page){
            Ad.get({"page":page},function(response) {
                $scope.ads = response.results;
                $scope.count_page = response.count;
                $scope.next_page = response.next;
                $scope.prev_page = response.previous;
            });
        };
        $scope.submitAd= function(text) {
            var ad = new Ad({text: text});
            ad.$save(function(){
                $scope.ads.unshift(ad);
            })
        }
        $scope.deleteAd= function(ad, index) {
            Ad.delete({id:ad.id}, function(index) {
                $scope.ads.splice(index,1);
            });
        }
    }
})();