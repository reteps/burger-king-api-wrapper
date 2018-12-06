#!/usr/bin/env python3
import requests
import xml.etree.ElementTree

BASE_URL = "http://bkm-cdn.tillster.com"
BASE_URL_2 = "https://bkm-native-prod.tillster.com"


class Promo:

    def __init__(self, data):
        self.promoCode = data["promoCode"]
        self.storePromoCode = data["storePromoCode"]
        self.startDate = data["startDate"]
        self.expirationDate = data["expirationDate"]
        self.remainingDays = data["remainingDays"]
        self.posSku = data["posSku"]
        self.maxRedemptions = data["maxRedemptions"]
        self.channel = data["channel"]
        self.orderDiscountPercentage = data["orderDiscountPercentage"]
        self.itemDiscountPercentage = data["itemDiscountPercentage"]
        self.orderFlatDiscountAmount = data["orderFlatDiscountAmount"]
        self.itemFlatDiscountAmount = data["itemFlatDiscountAmount"]
        self.mobilem8MenuSku = data["mobilem8MenuSku"]
        self.description = data["description"]
        self.displayName = data["displayName"]
        self.promoCodeType = data["promoCodeType"]
        self.parentPromoCodeId = data["parentPromoCodeId"]
        self.id = data["id"]
        self.medium = data["medium"]
        self.url = data["url"]
        self.loyaltyCost = data["loyaltyCost"]
        self.startDateTimeZone = data["startDateTimeZone"]
        self.expirationDateTimeZone = data["expirationDateTimeZone"]
        self.guestRedeemable = data["guestRedeemable"]
        self.offerType = data["offerType"]
        self.validModes = data["validModes"]
        self.props = Prop(data["props"])
        self.status = Status(data["status"])


class Status:
    def __init__(self, data):
        self.new = data["new"]


class Prop:
    def __init__(self, data):
        self.shortCodeImage = data["short_code_image"]
        self.couponImage = data["coupon_image"]
        self.priority = data["priority"]
        self.offerDetails = data["offer_details"]
        self.headline = data["headline"]
        self.menum8PruningPoint = data["menum8_pruning_point"]


def retrieveCoupons():
    url = BASE_URL_2 + "/mobile-aggregation-service/rest/coupons"
    allData = requests.get(url).json()
    return [Promo(d) for d in allData["loyaltyAppSession"]["promoOffers"]]


def getEndpoints():
    data = requests.get(BASE_URL).text
    parsed = xml.etree.ElementTree.XML(data)
    results = parsed.findall('.//{http://s3.amazonaws.com/doc/2006-03-01/}Key')
    return [r.text for r in results]

