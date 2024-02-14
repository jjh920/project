from sqlalchemy import insert, select, update, func, or_

from app.dbfactory import Session
from app.models.product import Product


class ProductService():
    @staticmethod
    def product_convert(pdto):
        data = pdto.model_dump()
        pd = Product(**data)
        data = {'name': pd.name, 'exp': pd.exp, 'detail': pd.detail,
                'retail': pd.retail, 'pctoff': pd.pctoff, 'useyn': pd.useyn,
                'tumbimg': pd.tumbimg, 'catnum': pd.catnum}
        return data

    @staticmethod
    def select_list():
        with Session() as sess:
            stmt = select(Product.prodnum, Product.name, Product.exp, Product.detail, Product.price, Product.tumbimg,
                          Product.catnum) \
                .order_by(Product.prodnum.desc()) \
                .offset(0).limit(20)
            result = sess.execute(stmt)
        return result

    @staticmethod
    def selectone_prod(prodnum):
        with Session() as sess:
            stmt = select(Product).filter_by(prodnum=prodnum)
            result = sess.execute(stmt).first()
        return result
