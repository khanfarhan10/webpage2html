#!/usr/bin/env python2

import os, sys, unittest
import webpage2html

class Test(unittest.TestCase):

    def local_test(self, index):
        print ''
        gen = webpage2html.generate(index).encode('utf8')
        ans = open(index[:-5] + '_single.html', 'rb').read()
        self.assertEqual(gen, ans, 'Test Fail for %s, ans = %s\ngen = %s\n' % (index, ans, gen))

    def test_0ops(self):
        self.local_test('./hacklu-ctf-2013-exp400-wannable-0ops.html')

    def test_meepo_download(self):
        self.local_test('./meepo-download.html')

    def test_packet_storm(self):
        self.local_test('./packet-storm-openssh-backdoor-patch.html')

    def test_none(self):
        print ''
        self.assertEqual(webpage2html.generate('non-existing-file.html'), '')

if __name__ == '__main__':
    if os.path.dirname(sys.argv[0]):
        os.chdir(os.path.dirname(sys.argv[0]))
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    rs = unittest.TextTestRunner(verbosity=2).run(suite)
    if len(rs.errors) > 0 or len(rs.failures) > 0:
        sys.exit(10)
    else:
        sys.exit(0)