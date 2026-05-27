# Async Loading Checklist

## Reference Strategy

- Use hard references for assets that must always load with the owner.
- Use soft references or Primary Asset IDs for optional, large, cosmetic, or mode-specific assets.
- Group related soft references into Asset Manager bundles when a feature loads as a unit.
- Check Primary Asset Rules, chunk IDs, and cook rules for assets discovered only by soft path.

## Load Flow

1. Validate the requested ID, row handle, soft object path, or Primary Asset ID.
2. Start async load through Asset Manager or `FStreamableManager`.
3. Store/cancel handles according to owner lifetime.
4. In completion callbacks, check UObject validity and failure paths.
5. Apply results on the game thread and broadcast a narrow success/failure event.

## Failure Modes

- Missing cooked asset.
- Asset class mismatch.
- Owner destroyed before callback.
- Duplicate concurrent requests racing to populate one cache.
- Save data points at a renamed row or asset.

## Verification

- Test editor PIE, standalone, and packaged build for soft-reference discovery.
- Include a missing asset/row case.
- Profile hitch risk for first-time loads and consider preloading at mode boundaries.
