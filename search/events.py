from workers.utils import CeleryTask

class SearchData(CeleryTask):
    events = 'simple_search'
    
    def run(self,ctx):
        super(SearchData,self).run(ctx)
        
class DetailSearchData(CeleryTask):
    events = 'detail_search'
    
    def run(self,ctx):
        super(DetailSearchData,self).run(ctx)
    