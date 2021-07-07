=====
prefix_verification
=====

prefix_verification is package that:
check the validity of a country code
given a nation return the prefix associated

Quick start
-----------

use the function verify_prefix

Given in input the country code relating to the nation and the prefix to be verified,
returned the validity of the prefix for that nation.

country_code: nation code id (Codice ISO 3166 alpha2)

prefix: prefix for country

return PrefixStatus object (Enum)

example:

from prefix_veirfication.utils import verify_prefix

country = 'IT'

prefix = '+39'

result = verify_prefix(country, prefix)

----------------------------------------------------------------------------------------------

use the function get_country_prefix

Given in input the country code relating to the nation, returned the prefix for that country.

country_code: nation code id (Codice ISO 3166 alpha2)

return Prefixes object (Enum) or None if there's not a match for country

example:

from prefix_verification.utils import get_country_prefix

country = 'IT'

result = get_country_prefix(country)
