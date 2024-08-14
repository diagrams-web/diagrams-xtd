import unittest
import config
from diagrams_xtd import cli


class CliTest(unittest.TestCase):
    """"""

    def test_read_provider_meta_file(self):
        """"""
        import random

        # pass a random valid provider
        # start at 1 to skip "base"
        provider_path = '%s/%s/' % (config.DIR_RESOURCE, config.PROVIDERS[random.randint(1, len(config.PROVIDERS) - 1)])
        content = cli._read_provider_meta_file(provider_path)
        # check that we have data
        self.assertTrue(content)

    def test_metas_with_one_provider(self):
        """"""
        # check with one provider
        providers = ['elastic']
        providers_metas = cli.metas(providers)

        # we have one result
        self.assertEqual(len(providers_metas), len(providers))
        # and this result is for the given provider
        self.assertEqual(list(providers_metas[0].keys()), providers)

    def test_metas_with_n_providers(self):
        """"""
        # check with n providers
        providers = ['elastic', 'digitalocean', 'k8s']
        providers.sort()
        providers_metas = cli.metas(providers)

        # we have n results
        self.assertEqual(len(providers_metas), len(providers))
        # and the result are for the given providers
        self.assertEqual([list(one_pvd.keys())[0] for one_pvd in providers_metas], providers)

    def test_metas_with_all(self):
        """"""
        providers = ['all']
        providers_metas = cli.metas(providers)
        provides_to_skip = 'base'
        all_providers = [pvd for pvd in config.PROVIDERS if pvd not in provides_to_skip]
        all_providers.sort()
        # we have all the providers
        self.assertEqual(len(providers_metas), len(all_providers))
        # and this result is for the given provider
        self.assertEqual([list(one_pvd.keys())[0] for one_pvd in providers_metas], all_providers)
