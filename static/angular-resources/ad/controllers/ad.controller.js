/**
 * AdCtrl
 * @namespace App.ad.controllers
 */
var temp;

(function () {
    'use strict';

    angular
        .module('App.ad.controllers')
        .controller('AdCtrl', AdCtrl);

    AdCtrl.$inject = ['$scope', 'Ad', 'Snackbar'];

    /**
     * @namespace AdCtrl
     */
    function AdCtrl($scope, Ad, Snackbar) {
        ////////// MAP //////////////
        $scope.map = {center: {latitude: -31.4179952, longitude: -64.1890513 }, zoom: 9 };
        $scope.options = {};
        $scope.control = {};

        $scope.callControl = function() {
            console.log("callControl");
            console.log($scope.control);
        }

        $scope.circle_events = {
            click: function (marker, eventName, args) {
                console.log(args.$parent.ad.pk);
                $('html, body').animate({
                    scrollTop: $("#ad-anchor-" + args.$parent.ad.pk).offset().top - 70
                }, 1000);
            },
            mouseover: function (marker, eventName, args) {
                args.$parent.ad.selected = true;
            },
            mouseout: function (marker, eventName, args) {
                args.$parent.ad.selected = false;
            }
        };

        $scope.location_options = {
            draggable: false, // optional: defaults to false
            clickable: true, // optional: defaults to true
            editable: false, // optional: defaults to false
            visible: true // optional: defaults to true
        }
        ///////// FIN MAP ////////////


        $scope.ads = {};
        $scope.next_page = null;
        $scope.prev_page = null;
        $scope.count_page = 0;
        $scope.current_page = 1;
        $scope.pages = [];

        getAds();

        function getAds(){
            Ad.get(function(data) {
                console.log("cargando datos");
                $scope.ads = data.results;

                $scope.next_page = data.next;
                $scope.prev_page = data.previous;

                // set Circle style for each ad
                $.each($scope.ads,function(index, ad){
                    setCircleStyle(ad);

                });
            });
        }

        function setCircleStyle(ad){
            if (ad.selected) {
                ad.stroke = {color: '#00FF00', weight: 2, opacity: 1 };
                ad.fill = {color: '#00AA00', weight: 2, opacity: 1 };
            } else {
                ad.stroke = {color: '#FF0000', weight: 2, opacity: 1 };
                ad.fill = {color: '#AA0000', weight: 2, opacity: 1 };
            }
        }

        $scope.selectAd = function (ad) {
            ad.selected = true;
            setCircleStyle(ad);
        }
        $scope.deselectAd = function (ad) {
            ad.selected = false;
            setCircleStyle(ad);
        }

        $scope.AddToFavourites = function(ad) {
            window.alert("NOT IMLPEMENTED YET! ad" + ad.pk + " should be added to favourites")
        }

        $scope.get_ads_page = function(page){
            Ad.get({"page":page},function(response) {
                $scope.current_page = page;
                $scope.ads = response.results;
                $scope.next_page = response.next;
                $scope.prev_page = response.previous;

                 // set Circle style for each ad
                $.each($scope.ads,function(index, ad){
                    setCircleStyle(ad);

                });
            });
        };

        $scope.changePage = function(){
            console.log("CAMBIO DE PAGINA! ");
        };

        $scope.submitAd= function(text) {
            var ad = new Ad({text: text});
            ad.$save(function(){
                $scope.ads.unshift(ad);
            })
        };

        $scope.deleteAd= function(ad) {

            Ad.delete({id:ad.id}, deleteSuccess, deleteError);

            function deleteSuccess(data, headers, status){
                getAds();
                //$scope.ads.splice($scope.ads.indexOf(ad),1);
                Snackbar.show("El aviso fue eliminado con exito!");
            }

            function deleteError(data, headers, status){
                Snackbar.error("Error al intentar borrar el aviso");
            }
        };
    }
})();