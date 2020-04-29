import { HhFrontPage } from './app.po';

describe('hh-front App', function() {
  let page: HhFrontPage;

  beforeEach(() => {
    page = new HhFrontPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
