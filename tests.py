from nose.tools import assert_equal
from textwrap import dedent

from html2text import html2text


def assert_convert(html, plaintext):
    html = dedent(html)
    plaintext = dedent(plaintext)
    assert_equal(html2text(html), plaintext)

def test_paragraph():
    assert_convert(
        '''\
            <p>test paragraph one</p>
            <p>test paragraph two</p>
        ''',
        '''\
            test paragraph one

            test paragraph two

        '''
    )

def test_heading():
    assert_convert(
        '''\
            <h1>one</h1>
            <h2>two</h2>
            <h3>three</h3>
            <h4>four</h4>
            <h5>five</h5>
        ''',
        '''\
            # one

            ## two

            ### three

            #### four

            ##### five

        '''
    )
