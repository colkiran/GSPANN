
class MyCompany:

    companyHead = ""

    @classmethod
    def set_comp_head(cls, chead):
        cls.companyHead = chead

    @classmethod
    def get_comp_head(cls):
        return cls.companyHead

MyCompany.set_comp_head("Micheal")
print(MyCompany.get_comp_head())
