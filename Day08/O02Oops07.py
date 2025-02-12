
class TaxCalc:

    def __init__(self, invno, total_cost):
        self.invno = invno
        self.total_cost = total_cost

    @staticmethod
    def gstCalc(state, invno, total_cost):
        if state == 'KAR':
            cgst = 0.09
            sgst = 0.09
            gst_amt = (cgst + sgst) * total_cost
        else:
            igst = 0.18
            gst_amt = igst * total_cost

        return gst_amt

    def get_details(self):
        gst_amt = self.gstCalc("KAR", self.invno, self.total_cost)
        return self.invno, gst_amt + self.total_cost

tc = TaxCalc("INV001", 75000)
print(tc.get_details())


