
//Could you tell us what's happening here;

const $ = cheerio.load(pm.response.text());

pm.test("It should load the submission", () => {
   const element = $.html('body > div.container > h3')
   pm.expect($('title').text()).to.not.be.empty   
   let uuid = pm.environment.get("UUID_1")
   pm.expect(element).to.include(uuid)
})